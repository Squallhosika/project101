package com.unicorn.userui.activity;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;

import com.unicorn.apigateway.ApiGateway;
import com.unicorn.apigateway.model.Item;
import com.unicorn.apigateway.model.Order;
import com.unicorn.userui.R;
import com.unicorn.userui.adapter.MenuAdapter;
import com.unicorn.userui.adapter.OrderBookAdapter;

import java.util.List;

/**
 * Created by jonathan on 23/10/17.
 */

public class OrderBookActivity extends AppCompatActivity {
    private RecyclerView mRecyclerView;
    private OrderBookAdapter mAdapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mRecyclerView = (RecyclerView) findViewById(R.id.rv_main);
        LinearLayoutManager layoutManager = new LinearLayoutManager(this, LinearLayoutManager.VERTICAL, false);
        mRecyclerView.setLayoutManager(layoutManager);
        mRecyclerView.setHasFixedSize(true);

        List<Order> orders = (List<Order>) ApiGateway.call("getOrders", null);
        mAdapter = new OrderBookAdapter(orders);
        mRecyclerView.setAdapter(mAdapter);

    }
}
