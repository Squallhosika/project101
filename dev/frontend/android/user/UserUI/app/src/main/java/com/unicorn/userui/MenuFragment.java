package com.unicorn.userui;

import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;

public class MenuFragment extends Fragment {

    @Override
    public void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        String[] values = {"Item1","Item2","Item3","Item4","Item5"};
        ArrayAdapter adapter = new ArrayAdapter<String>(getActivity().getApplicationContext(),R.layout.list_view_main, R.id.firstLine,values);
//        ListView listView = (ListView) getActivity().findViewById(R.id.listview_menu);
        ListView listView = (ListView) getActivity().findViewById(R.id.listview);
        listView.setAdapter(adapter);
        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
//                MenuFragment newFragment = new MenuFragment();
//                getActivity().getSupportFragmentManager().beginTransaction().replace(R.id.fragment_container, newFragment).commit();
            }
        });
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        return inflater.inflate(R.layout.fragment_menu, container, false);
    }

}
