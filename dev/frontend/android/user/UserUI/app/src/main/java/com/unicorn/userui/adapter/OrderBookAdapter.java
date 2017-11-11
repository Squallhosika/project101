package com.unicorn.userui.adapter;

import android.content.Intent;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import android.content.Context;

import com.unicorn.apigateway.model.Order;
import com.unicorn.userui.R;
import com.unicorn.userui.activity.OrderCardActivity;

import java.util.List;

/**
 * Created by jonathan on 23/10/17.
 */

public class OrderBookAdapter extends RecyclerView.Adapter<OrderBookAdapter.ViewHolder>{

    private List<Order> orders;
    private Context mContext;

    public OrderBookAdapter(List<Order> orders) {
        this.orders = orders;
    }

    @Override
    public ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        LayoutInflater inflater = LayoutInflater.from(parent.getContext());
        View v = inflater.inflate(R.layout.rv_orderbook_order, parent, false);

        ViewHolder viewHolder = new ViewHolder(v);
        return viewHolder;
    }

    @Override
    public void onBindViewHolder(ViewHolder holder, int position) {
        final String orderId = orders.get(position).getId();
//        final String description = orders.get(position).getDescription();


//        holder.tvOrderName.setText(orderId);
//        holder.tvOrderName.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View v) {
//                openOrderCard()
//            }
//        });
//
//        holder.tvOrderDescription.setText(description);

    }

    @Override
    public int getItemCount() {
        return orders.size();
    }

    public class ViewHolder extends RecyclerView.ViewHolder {
        public TextView tvOrderId;
//        public TextView tvOrderDescription;

        public ViewHolder(View itemView) {
            super(itemView);
            tvOrderId = (TextView) itemView.findViewById(R.id.order_name);

            tvOrderId.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    String orderId = tvOrderId.getText().toString();
                    openOrderCard(orderId);
                }
            });
//            tvOrderDescription = (TextView) itemView.findViewById(R.id.order_description);
        }
    }

    private void openOrderCard(String orderId) {
        Intent intent = new Intent(mContext, OrderCardActivity.class);
        intent.putExtra("orderId", orderId);
        mContext.startActivity(intent);
    }


}
