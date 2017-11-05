package com.unicorn.apigateway.model;

import java.io.Serializable;

/**
 * Created by jonathan on 23/10/17.
 */

public class Item implements Serializable {

    private final String id;
    private final String name;
    private final String description;
    // private final double price;

    public Item(String id, String name, String description) {
        this.id = id;
        this.name = name;
        this.description = description;
    }

    public String getId() {
        return this.id;
    }

    public String getName() {
        return this.name;
    }

    public String getDescription() {
        return description;
    }

    @Override
    public String toString() {
        return "Item{" +
                "id='" + id + '\'' +
                ", name='" + name + '\'' +
                ", description='" + description + '\'' +
                '}';
    }
}

