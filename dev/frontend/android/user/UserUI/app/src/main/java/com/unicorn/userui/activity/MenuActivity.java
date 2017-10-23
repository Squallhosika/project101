package com.unicorn.userui.activity;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;

import com.unicorn.apigateway.ApiGateway;
import com.unicorn.apigateway.model.Client;
import com.unicorn.apigateway.model.Item;
import com.unicorn.userui.R;
import com.unicorn.userui.adapter.MainAdapter;
import com.unicorn.userui.adapter.MenuAdapter;

import java.util.List;

/**
 * Created by jonathan on 23/10/17.
 */

public class MenuActivity extends AppCompatActivity {
    private RecyclerView mRecyclerView;
    private MenuAdapter mAdapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mRecyclerView = (RecyclerView) findViewById(R.id.rv_main);
        LinearLayoutManager layoutManager = new LinearLayoutManager(this, LinearLayoutManager.VERTICAL, false);
        mRecyclerView.setLayoutManager(layoutManager);
        mRecyclerView.setHasFixedSize(true);

        List<Item> items = (List<Item>) ApiGateway.call("getItems", null);
        mAdapter = new MenuAdapter(items);
        mRecyclerView.setAdapter(mAdapter);

    }
}
