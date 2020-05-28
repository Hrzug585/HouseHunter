package com.example.HouseHunter.service;

import com.example.HouseHunter.model.Home;
import org.springframework.data.elasticsearch.core.ElasticsearchOperations;
import org.springframework.data.elasticsearch.core.query.IndexQueryBuilder;
import org.springframework.stereotype.Service;

@Service
public class HomeService {

    private ElasticsearchOperations elasticsearchOperations;
    private IndexQueryBuilder indexQueryBuilder;

    public HomeService(ElasticsearchOperations elasticsearchOperations) {
        this.elasticsearchOperations = elasticsearchOperations;
        this.indexQueryBuilder = new IndexQueryBuilder();
    }

    public void save(Home home){
        indexQueryBuilder.withId(home.getId().toString()).withObject(home).build();
        elasticsearchOperations.save(home);
    }

    public Home findById(String id){
        return elasticsearchOperations.get(id, Home.class);
    }

}
