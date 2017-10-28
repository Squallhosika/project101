package com.unicorn.userui.activity;

import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.design.widget.BottomNavigationView;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.support.v7.widget.Toolbar;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.AdapterView;

import com.unicorn.apigateway.ApiGateway;
import com.unicorn.apigateway.model.Client;
import com.unicorn.apigateway.model.Item;
import com.unicorn.apigateway.model.Order;
import com.unicorn.userui.R;
import com.unicorn.userui.adapter.MainAdapter;
import com.unicorn.userui.adapter.MenuAdapter;
import com.unicorn.userui.adapter.OrderBookAdapter;

import java.util.List;

public class MainActivity extends AppCompatActivity {

    private Toolbar mToolbar;
    private RecyclerView mRecyclerView;
    private RecyclerView.Adapter mAdapter;
    private BottomNavigationView.OnNavigationItemSelectedListener mOnNavigationItemSelectedListener;

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

        mToolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(mToolbar);

        BottomNavigationView bottomNavigationView = (BottomNavigationView) findViewById(R.id.bottom_navigation);
        bottomNavigationView.setOnNavigationItemSelectedListener(getBottomNavigationListener());

    }


    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_toolbar, menu);
        return true;
    }


    private BottomNavigationView.OnNavigationItemSelectedListener getBottomNavigationListener(){
        return new BottomNavigationView.OnNavigationItemSelectedListener() {

            @Override
            public boolean onNavigationItemSelected(@NonNull MenuItem item) {
                switch (item.getItemId()) {

                    case R.id.navigation_home:
                        openMain();
                        break;

                    case R.id.navigation_dashboard:
                        openOrderBook();
                        break;

                    case R.id.navigation_notifications:
                        openOrderCard();
                        break;

                }
                return true;
            }

        };
    }





    private void openMain() {
    }

    private void openMenu(){
        Intent intent = new Intent(this, MenuActivity.class);
        startActivity(intent);
        this.overridePendingTransition(0, 0);
    }

    private void openOrderBook() {
        Intent intent = new Intent(this, OrderBookActivity.class);
        startActivity(intent);
        this.overridePendingTransition(0, 0);
    }

    private void openOrderCard() {
        Intent intent = new Intent(this, OrderCardActivity.class);
        int id = 10;
        intent.putExtra("orderId", id);
        startActivity(intent);
        this.overridePendingTransition(0, 0);
    }
}
