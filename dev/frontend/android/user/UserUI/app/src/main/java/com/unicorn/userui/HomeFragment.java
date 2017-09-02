package com.unicorn.userui;

import android.os.AsyncTask;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.support.v4.app.ListFragment;
import android.util.JsonReader;
import android.view.LayoutInflater;
import android.view.MenuItem;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;

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

//        AsyncTask.execute(new Runnable() {
//            @Override
//            public void run() {
//                // Create URL
//                URL githubEndpoint = null;
//                try {
//                    githubEndpoint = new URL("http://localhost:8000/geo/clientsaround");
//                    // Create connection
//                    HttpsURLConnection myConnection =
//                            (HttpsURLConnection) githubEndpoint.openConnection();
//
//                    if (myConnection.getResponseCode() == 200) {
//                        // Success
//                        InputStream responseBody = myConnection.getInputStream();
//                        InputStreamReader responseBodyReader =
//                                new InputStreamReader(responseBody, "UTF-8");
//                        JsonReader jsonReader = new JsonReader(responseBodyReader);
//
//
//                    } else {
//                        // Error handling code goes here
//                    }
//
//                } catch (MalformedURLException e) {
//                    e.printStackTrace();
//                } catch (IOException e) {
//                    e.printStackTrace();
//                }
//
//
//            }
//        });

        getContent();
        run();

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



    private void run(){
        AsyncTask.execute(new Runnable() {
            @Override
            public void run() {
                try {
                    URL endpoint = new URL("http://localhost:8000/geo/clientsaround");
                } catch (MalformedURLException e) {
                    e.printStackTrace();
                }
            }
        });
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

//    @Override
//    public void onListItemClick(ListView l, View v, int position, long id) {
//        super.onListItemClick(l, v, position, id);
//        MenuFragment newFragment = new MenuFragment();
//        getActivity().getSupportFragmentManager().beginTransaction().replace(R.id.fragment_container, newFragment).commit();
//    }
}
