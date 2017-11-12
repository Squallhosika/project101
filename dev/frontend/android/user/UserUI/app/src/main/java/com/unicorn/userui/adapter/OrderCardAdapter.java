package com.unicorn.userui.adapter;

import android.content.Context;
import android.content.Intent;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import com.unicorn.apigateway.model.Basket;
import com.unicorn.apigateway.model.Item;
import com.unicorn.apigateway.model.Order;
import com.unicorn.userui.R;
import com.unicorn.userui.activity.ItemCardActivity;

import java.util.List;

/**
 * Created by jonathan on 23/10/17.
 */

public class OrderCardAdapter extends RecyclerView.Adapter<OrderCardAdapter.ViewHolder> {

    private Context mContext;
    private Order order;

    public OrderCardAdapter(Order order) {
        this.order = order;
    }

    @Override
    public ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        LayoutInflater inflater = LayoutInflater.from(parent.getContext());
        View v = inflater.inflate(R.layout.rv_ordercard_item, parent, false);

        ViewHolder viewHolder = new ViewHolder(v);
        return viewHolder;
    }

    @Override
    public void onBindViewHolder(ViewHolder holder, int position) {
        final String id = order.getBasket().getOrderLines().get(position).getItem().getId();
        final String name = order.getBasket().getOrderLines().get(position).getItem().getName();
        final String description = order.getBasket().getOrderLines().get(position).getItem().getDescription();
        final double unitPrice = order.getBasket().getOrderLines().get(position).getPrice();
        final int quantity = order.getBasket().getOrderLines().get(position).getQuantity();

        holder.itemId = id;
        holder.tvItemName.setText(name);
        holder.tvItemDescription.setText(description);
        holder.tvUnitPrice.setText(String.format("Price:£%1$,.2f", unitPrice));
        holder.tvQuantity.setText("Quantity:" +  Integer.toString(quantity));
    }

    @Override
    public int getItemCount() {
        return order.getBasket().getOrderLines().size();
    }

    public class ViewHolder extends RecyclerView.ViewHolder {
        public String itemId;
        public ImageView ivItemImage;
        public TextView tvItemName;
        public TextView tvItemDescription;
        public TextView tvUnitPrice;
        public TextView tvQuantity;

        public ViewHolder(View itemView) {
            super(itemView);
            ivItemImage = (ImageView) itemView.findViewById(R.id.iv_ordercard_itemimg);
            tvItemName = (TextView) itemView.findViewById(R.id.tv_ordercard_itemname);
            tvItemDescription = (TextView) itemView.findViewById(R.id.tv_ordercard_itemdesc);
            tvUnitPrice = (TextView) itemView.findViewById(R.id.tv_ordercard_itemprice);
            tvQuantity = (TextView) itemView.findViewById(R.id.tv_ordercard_itemqty);

            mContext = itemView.getContext();

            itemView.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    openItemCard(itemId);
                }
            });

        }
    }

    private void openItemCard(String itemId) {
        Intent intent = new Intent(mContext, ItemCardActivity.class);
        intent.putExtra("itemId", itemId);
        mContext.startActivity(intent);
    }
}
