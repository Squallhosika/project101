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
import com.unicorn.apigateway.model.OrderLine;
import com.unicorn.userui.R;
import com.unicorn.userui.activity.ItemCardActivity;
import com.unicorn.userui.activity.MenuActivity;

import java.util.List;

/**
 * Created by jonathan on 23/10/17.
 */

public class MenuAdapter extends RecyclerView.Adapter<MenuAdapter.ViewHolder> {

    private Context mContext;
    private Basket basket;

    public MenuAdapter(Basket basket) {
        this.basket = basket;
    }

    @Override
    public ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        LayoutInflater inflater = LayoutInflater.from(parent.getContext());
        View v = inflater.inflate(R.layout.rv_menu_item, parent, false);

        ViewHolder viewHolder = new ViewHolder(v);
        return viewHolder;
    }

    @Override
    public void onBindViewHolder(ViewHolder holder, int position) {
        final String name = basket.getOrderLines().get(position).getItem().getName();
        final String description = basket.getOrderLines().get(position).getItem().getDescription();
        final double price = basket.getOrderLines().get(position).getPrice();
        int quantity = basket.getOrderLines().get(position).getQuantity();

        holder.itemId = basket.getOrderLines().get(position).getItem().getId();
        holder.tvItemName.setText(name);
        holder.tvItemDescription.setText(description);
        holder.tvItemPrice.setText(String.format("£%1$,.2f", price));
        holder.tvItemQuantity.setText(Integer.toString(quantity));
    }

    @Override
    public int getItemCount() {
        return basket.getOrderLines().size();
    }

    public class ViewHolder extends RecyclerView.ViewHolder {
        public String itemId;
        public ImageView ivItemImage;
        public ImageView ivAddItem;
        public ImageView ivRemoveItem;
        public TextView tvItemName;
        public TextView tvItemDescription;
        public TextView tvItemPrice;
        public TextView tvItemQuantity;

        public ViewHolder(View itemView) {
            super(itemView);
            ivItemImage = itemView.findViewById(R.id.item_image);
            tvItemName = itemView.findViewById(R.id.item_name);
            tvItemDescription = itemView.findViewById(R.id.item_description);
            ivAddItem = itemView.findViewById(R.id.btn_plus);
            ivRemoveItem = itemView.findViewById(R.id.btn_minus);
            tvItemPrice =  itemView.findViewById(R.id.tv_menu_item_price);
            tvItemQuantity = itemView.findViewById(R.id.tv_menu_item_quantity);

            mContext = itemView.getContext();

            ivItemImage.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    openItemCard(itemId);
                }
            });

            ivAddItem.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    String itemName = tvItemName.getText().toString();
                    String itemDescription = tvItemDescription.getText().toString();

                    Item item = new Item(itemId, itemName, itemDescription);
                    OrderLine line = basket.addItem(item);
                    tvItemQuantity.setText(Integer.toString(line.getQuantity()));
                }
            });

            ivRemoveItem.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    String itemName = tvItemName.getText().toString();
                    String itemDescription = tvItemDescription.getText().toString();

                    Item item = new Item(itemId, itemName, itemDescription);
                    OrderLine line = basket.removeItem(item);
                    tvItemQuantity.setText(Integer.toString(line.getQuantity()));
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
