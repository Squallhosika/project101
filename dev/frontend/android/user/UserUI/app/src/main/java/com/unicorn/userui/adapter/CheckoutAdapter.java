package com.unicorn.userui.adapter;

import android.content.Context;
import android.content.Intent;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import com.unicorn.apigateway.model.Basket;
import com.unicorn.apigateway.model.Item;
import com.unicorn.apigateway.model.OrderLine;
import com.unicorn.userui.R;
import com.unicorn.userui.activity.ItemCardActivity;

import java.util.List;

/**
 * Created by jonathan on 23/10/17.
 */

public class CheckoutAdapter extends RecyclerView.Adapter<CheckoutAdapter.ViewHolder>{

    private Context mContext;
    private List<OrderLine> orderLines;
    private Basket basket;

    public CheckoutAdapter(Basket basket) {
//        this.basket = basket;
        this.orderLines = basket.getOrderLines();
    }

    @Override
    public ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        LayoutInflater inflater = LayoutInflater.from(parent.getContext());
        View v = inflater.inflate(R.layout.rv_checkout_item, parent, false);

        ViewHolder viewHolder = new ViewHolder(v);
        return viewHolder;
    }

    @Override
    public void onBindViewHolder(ViewHolder holder, int position) {
        final String id = orderLines.get(position).getItem().getId();
        final String name = orderLines.get(position).getItem().getName();
        final String description = orderLines.get(position).getItem().getDescription();
        final double price = orderLines.get(position).getPrice();
        final int quantity = orderLines.get(position).getQuantity();

        holder.tvItemId.setText(id);
        holder.tvItemName.setText(name);
        holder.tvItemDescription.setText(quantity + " of " + description + " @ " + price);
        holder.tvPrice.setText(Double.toString(price));
        holder.tvQuantity.setText(Integer.toString(quantity));


    }

    @Override
    public int getItemCount() {
        return orderLines.size();
    }

    public class ViewHolder extends RecyclerView.ViewHolder {
        public TextView tvItemId;
        public TextView tvItemName;
        public TextView tvItemDescription;
        public TextView tvPrice;
        public TextView tvQuantity;

        public ViewHolder(View itemView) {
            super(itemView);
            tvItemId = (TextView) itemView.findViewById(R.id.tv_checkout_item_id);
            tvItemName = (TextView) itemView.findViewById(R.id.tv_checkout_item_name);
            tvItemDescription = (TextView) itemView.findViewById(R.id.tv_checkout_item_description);
            tvPrice = (TextView) itemView.findViewById(R.id.tv_checkout_item_price);
            tvQuantity = (TextView) itemView.findViewById(R.id.tv_checkout_item_quantity);

            mContext = itemView.getContext();

//            itemView.setOnClickListener(new View.OnClickListener() {
//                @Override
//                public void onClick(View view) {
//                    openItemCard(tvItemId.getText().toString());
//                }
//            });
        }
    }

    private void openItemCard(String itemId) {
        Intent intent = new Intent(mContext, ItemCardActivity.class);
        intent.putExtra("itemId", itemId);
        mContext.startActivity(intent);
    }
}
