package com.unicorn.userui.api;

import android.app.Activity;
import android.content.Context;
import android.os.AsyncTask;
import android.util.Log;
import android.widget.ListView;
import android.widget.TextView;

import com.unicorn.userui.R;
import com.unicorn.userui.model.Client;
import com.unicorn.userui.model.Greeting;

import org.springframework.http.converter.json.MappingJackson2HttpMessageConverter;
import org.springframework.web.client.RestTemplate;

/**
 * Created by Keuvin on 09/09/2017.
 */

public class HttpRequestTask extends AsyncTask<Void, Void, Greeting> {

    private Activity activity;
    private Context context;

    public HttpRequestTask(Context context) {
        this.context = context;
        this.activity = (Activity) context;
    }

    @Override
    protected Greeting doInBackground(Void... params) {
        Greeting greeting = null;
        try {
            final String url = "http://rest-service.guides.spring.io/greeting";
            RestTemplate restTemplate = new RestTemplate();
            restTemplate.getMessageConverters().add(new MappingJackson2HttpMessageConverter());
            greeting = restTemplate.getForObject(url, Greeting.class);
            return greeting;
        } catch (Exception e) {
            Log.e("MainActivity", e.getMessage(), e);
        }

        return greeting;
    }

    @Override
    protected void onPostExecute(Greeting greeting) {
        ListView listView = (ListView) activity.findViewById(R.id.listview);
        listView.getItemIdAtPosition(0);

        TextView tv = (TextView) activity.findViewById(R.id.firstLine);
        tv.setText(greeting.getContent());
    }
}
