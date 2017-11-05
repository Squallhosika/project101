package com.unicorn.apigateway.model;

/**
 * Created by jonathan on 04/11/17.
 */

public class OrderLine {

    private final Item item;
    private final double price;
    private final int quantity;

    public OrderLine(Item item, double price, int quantity) {
        this.item = item;
        this.price = price;
        this.quantity = quantity;
    }

    public Item getItem() {
        return item;
    }

    public double getPrice() {
        return price;
    }

    public int getQuantity() {
        return quantity;
    }
}
