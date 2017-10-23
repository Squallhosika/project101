package com.unicorn.userui.activity;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;

import com.unicorn.apigateway.ApiGateway;
import com.unicorn.apigateway.model.Client;
import com.unicorn.userui.R;
import com.unicorn.userui.adapter.MainAdapter;

import java.util.List;

public class MainActivity extends AppCompatActivity {

    private RecyclerView mRecyclerView;
    private MainAdapter mAdapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mRecyclerView = (RecyclerView) findViewById(R.id.rv_main);
        LinearLayoutManager layoutManager = new LinearLayoutManager(this, LinearLayoutManager.VERTICAL, false);
        mRecyclerView.setLayoutManager(layoutManager);
        mRecyclerView.setHasFixedSize(true);

        List<Client> clients = (List<Client>) ApiGateway.call("getClients", null);
        mAdapter = new MainAdapter(clients);
        mRecyclerView.setAdapter(mAdapter);

    }
}
