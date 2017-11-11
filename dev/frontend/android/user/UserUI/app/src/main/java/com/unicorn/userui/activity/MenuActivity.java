package com.unicorn.userui.activity;

import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.design.widget.BottomNavigationView;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.support.v7.widget.Toolbar;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.ImageButton;

import com.unicorn.apigateway.ApiGateway;
import com.unicorn.apigateway.model.Basket;
import com.unicorn.apigateway.model.Item;
import com.unicorn.userui.R;
import com.unicorn.userui.adapter.MenuAdapter;

import java.util.List;

/**
 * Created by jonathan on 23/10/17.
 */

public class MenuActivity extends AppCompatActivity {

    private Toolbar mToolbar;
    private RecyclerView mRecyclerView;
    private RecyclerView.Adapter mAdapter;
    private BottomNavigationView.OnNavigationItemSelectedListener mOnNavigationItemSelectedListener;
    private ImageButton mButtonBasket;

    private Basket basket;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_menu);


        mRecyclerView = (RecyclerView) findViewById(R.id.rv_menu);
        LinearLayoutManager layoutManager = new LinearLayoutManager(this, LinearLayoutManager.VERTICAL, false);
        mRecyclerView.setLayoutManager(layoutManager);
        mRecyclerView.setHasFixedSize(true);

        Intent intent = getIntent();
        String id = intent.getStringExtra("clientId");


        basket = new Basket(id);

        List<Item> items = (List<Item>) ApiGateway.call("getMenu", id);
        System.out.println(items);
        mAdapter = new MenuAdapter(items, basket);
        mRecyclerView.setAdapter(mAdapter);

        mToolbar = (Toolbar) findViewById(R.id.toolbar_widget);
        setSupportActionBar(mToolbar);
        getSupportActionBar().setDisplayHomeAsUpEnabled(true);
        
        mButtonBasket = (ImageButton) findViewById(R.id.btn_basket);
        mButtonBasket.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                openCheckout(basket);
            }
        });

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

    private void openCheckout(Basket basket){
        Intent intent = new Intent(this, CheckoutActivity.class);
        intent.putExtra("menuId", "10");
        intent.putExtra("basket", basket);
        startActivity(intent);
    }

    private void openOrderCard(){
        Intent intent = new Intent(this, OrderCardActivity.class);
        int id = 10;
        intent.putExtra("orderId", id);
        startActivity(intent);
    }

    private void openOrderBook() {
        Intent intent = new Intent(this, OrderBookActivity.class);
        startActivity(intent);
    }

    private void openMain() {
        Intent intent = new Intent(this, ClientBookActivity.class);
        startActivity(intent);
    }
}
