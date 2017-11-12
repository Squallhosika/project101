package com.unicorn.userui.adapter;

import android.content.Intent;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
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

        return new ViewHolder(v);
    }

    @Override
    public void onBindViewHolder(ViewHolder holder, int position) {
        final String orderId = orders.get(position).getId();
         holder.tvOrderId.setText(orderId);
    }

    @Override
    public int getItemCount() {
        return orders.size();
    }

    public class ViewHolder extends RecyclerView.ViewHolder {
        public TextView tvOrderId;
        public ImageView ivOrderImage;

        public ViewHolder(View itemView) {
            super(itemView);
            tvOrderId = (TextView) itemView.findViewById(R.id.order_name);
            ivOrderImage = (ImageView) itemView.findViewById(R.id.order_image);

            mContext = itemView.getContext();

            itemView.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    String orderId = tvOrderId.getText().toString();
                    openOrderCard(orderId);
                }
            });
        }
    }

    private void openOrderCard(String orderId) {
        Intent intent = new Intent(mContext, OrderCardActivity.class);
        intent.putExtra("orderId", orderId);
        mContext.startActivity(intent);
    }


}
