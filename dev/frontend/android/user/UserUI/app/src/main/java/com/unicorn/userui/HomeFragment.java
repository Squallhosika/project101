package com.unicorn.userui;

import android.os.AsyncTask;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.support.v4.app.ListFragment;
import android.util.JsonReader;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.MenuItem;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.TextView;

import org.springframework.http.converter.json.MappingJackson2HttpMessageConverter;
import org.springframework.web.client.RestTemplate;

import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.MalformedURLException;
import java.net.URL;

import javax.net.ssl.HttpsURLConnection;

public class HomeFragment extends Fragment {

    private String[] values;

    @Override
    public void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getContent();

        ArrayAdapter adapter = new ArrayAdapter<String>(getActivity().getApplicationContext(),R.layout.list_view_main, R.id.firstLine,this.values);
        ListView listView = (ListView) getActivity().findViewById(R.id.listview);
        listView.setAdapter(adapter);
        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                MenuFragment newFragment = new MenuFragment();
                getActivity().getSupportFragmentManager().beginTransaction().replace(R.id.fragment_container, newFragment).commit();
            }
        });
    }



    private class HttpRequestTask extends AsyncTask<Void, Void, Greeting> {
        @Override
        protected Greeting doInBackground(Void... params) {
            try {
                final String url = "http://rest-service.guides.spring.io/greeting";
                RestTemplate restTemplate = new RestTemplate();
                restTemplate.getMessageConverters().add(new MappingJackson2HttpMessageConverter());
                Greeting greeting = restTemplate.getForObject(url, Greeting.class);
                return greeting;
            } catch (Exception e) {
                Log.e("MainActivity", e.getMessage(), e);
            }

            return null;
        }

        @Override
        protected void onPostExecute(Greeting greeting) {
            TextView greetingIdText = (TextView) getActivity().findViewById(R.id.id_value);
            TextView greetingContentText = (TextView) getActivity().findViewById(R.id.content_value);
            greetingIdText.setText(greeting.getId());
            greetingContentText.setText(greeting.getContent());
        }

    }

    private class Greeting{
        private String id;
        private String content;

        public Greeting(String id, String content){

            this.id = id;
            this.content = content;
        }

        public String getId() {
            return id;
        }

        public void setId(String id) {
            this.id = id;
        }

        public String getContent() {
            return content;
        }

        public void setContent(String content) {
            this.content = content;
        }
    }



    private void getContent()
    {
        // the request
        String[] values = {"Android","IPhone","WindowsMobile","Blackberry",
                "WebOS","Ubuntu","Windows7","Max OS X","IPhone","WindowsMobile","Blackberry",
                "WebOS","Ubuntu","Windows7","Max OS X"};

        this.values=values;
    }


//    @Override
//    public void onActivityCreated(@Nullable Bundle savedInstanceState) {
//        super.onActivityCreated(savedInstanceState);
//        String[] values = {"Android","IPhone","WindowsMobile","Blackberry",
//                "WebOS","Ubuntu","Windows7","Max OS X","IPhone","WindowsMobile","Blackberry",
//                "WebOS","Ubuntu","Windows7","Max OS X"};
//        ArrayAdapter adapter = new ArrayAdapter<String>(getActivity().getApplicationContext(),R.layout.list_view_main, R.id.firstLine,values);
//
//        setListAdapter(adapter);
////        getListView().setOnItemClickListener(this);
//    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        return inflater.inflate(R.layout.fragment_home, container, false);
    }


    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            new HttpRequestTask().execute();
            return true;
        }

        return super.onOptionsItemSelected(item);
    }


//    @Override
//    public void onListItemClick(ListView l, View v, int position, long id) {
//        super.onListItemClick(l, v, position, id);
//        MenuFragment newFragment = new MenuFragment();
//        getActivity().getSupportFragmentManager().beginTransaction().replace(R.id.fragment_container, newFragment).commit();
//    }
}
