package com.unicorn.apigateway.model;

import java.io.Serializable;

/**
 * Created by jonathan on 23/10/17.
 */

public class Order implements Serializable {

    private final String id;
    private final Basket basket;

    public Order(String id, Basket basket) {
        this.id = id;
        this.basket = basket;
    }

    public String getId() {
        return this.id;
    }
    public Basket getBasket() {
        return basket;
    }
}

