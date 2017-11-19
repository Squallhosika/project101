package com.unicorn.apigateway.model;

import java.io.Serializable;

/**
 * Created by jonathan on 04/11/17.
 */

public class OrderLine implements Serializable {

    private final Item item;
    private final double price;
    private int quantity;

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

    public void addOne() {
        quantity = quantity + 1;
    }

    public void removeOne() {
        quantity = quantity - 1;
    }

    public void setQuanityZero() {
        quantity = 0;
    }

    public OrderLine copy() {
        return new OrderLine(item, price, quantity);
    }

}
