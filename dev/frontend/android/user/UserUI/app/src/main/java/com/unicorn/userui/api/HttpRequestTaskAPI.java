package com.unicorn.userui.api;

import android.app.Activity;
import android.content.Context;
import android.os.AsyncTask;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentTransaction;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.widget.ListView;
import android.widget.TextView;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import com.unicorn.userui.HomeFragment;
import com.unicorn.userui.MainActivity;
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

    private MainActivity activity;
    private HomeFragment nFragment;
    private Context context;
    private String URL = "http://147.135.189.68:8000";

    public HttpRequestTaskAPI(Context context, HomeFragment nFragment) {
        this.context = context;
        this.activity = (MainActivity) context;
        this.nFragment = nFragment;
    }

    @Override
    protected List<Client> doInBackground(Object... params) {
        List<Client> clients = null;
        try {
//            final String url = "http://10.0.2.2:8000/geo/clientsaround";
//            final String urlString = "http://10.0.2.2:8000/client/clients";
            final String urlString = URL + "/client/clients";


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
    protected void onPostExecute(List<Client> clients) {
        if(clients != null){
//            HomeFragment newFragment = new HomeFragment();
//            newFragment.refresh(clients);
            nFragment.refresh(clients);

//            this.activity.replaceFragment(nFragment);
//            this.activity.addFragment(nFragment);

//            activity.getSupportFragmentManager().beginTransaction().add(R.id.fragment_container,nFragment).commit();

//            FragmentTransaction transaction = activity.getSupportFragmentManager().beginTransaction();
//            transaction.add(R.id.fragment_container,nFragment, "home");
//            transaction.replace(R.id.fragment_container,nFragment, "home");
//            transaction.addToBackStack("home");

//            transaction.commit();

        }

//        ListView listView = (ListView) activity.findViewById(R.id.listview);
//        listView.getItemIdAtPosition(0);
//
//        TextView tv = (TextView) activity.findViewById(R.id.firstLine);
//        tv.setText(clients.get(0).getName());
    }

}
