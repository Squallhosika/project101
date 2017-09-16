package com.unicorn.userui.api;

import android.app.Activity;
import android.content.Context;
import android.os.AsyncTask;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentTransaction;
import android.util.Log;
import android.widget.ListView;
import android.widget.TextView;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import com.unicorn.userui.R;
import com.unicorn.userui.model.Client;
import com.unicorn.userui.response.ClientsResponse;

import org.springframework.http.converter.json.MappingJackson2HttpMessageConverter;
import org.springframework.web.client.RestTemplate;

import java.lang.reflect.Type;
import java.util.List;

import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

/**
 * Created by Keuvin on 09/09/2017.
 */

public class HttpRequestTaskAPI extends AsyncTask<Object, Object, List<Client>> {

    private Activity activity;
    private Context context;

    public HttpRequestTaskAPI(Context context) {
        this.context = context;
        this.activity = (Activity) context;
    }

    @Override
    protected List<Client> doInBackground(Object... params) {
        List<Client> clients = null;
        try {
//            final String url = "http://10.0.2.2:8000/geo/clientsaround";
            final String urlString = "http://10.0.2.2:8000/client/clients";


            OkHttpClient client = new OkHttpClient();
            Request request = new Request.Builder()
                        .url(urlString)
                        .build();

            Response response = client.newCall(request).execute();

            Type listType = new TypeToken<List<Client>>() {}.getType();
            clients = new Gson().fromJson(response.body().string(), listType);

            return clients;
        } catch (Exception e) {
            Log.e("MainActivity", e.getMessage(), e);
        }

        return clients;
    }

    @Override
    protected void onPostExecute(List<Client> client) {
        ListView listView = (ListView) activity.findViewById(R.id.listview);
        listView.getItemIdAtPosition(0);

        TextView tv = (TextView) activity.findViewById(R.id.firstLine);
        tv.setText(client.get(0).getName());
    }

    protected void refresh(){
        android.app.Fragment currentFragment = activity.getFragmentManager().findFragmentById(R.id.fragment_container);

        android.app.FragmentTransaction fragTransaction = activity.getFragmentManager().beginTransaction();
        fragTransaction.detach(currentFragment);
        fragTransaction.attach(currentFragment);
        fragTransaction.commit();
    }
}
