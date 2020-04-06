import { Component, OnInit } from '@angular/core';
import { Product } from '../interfaces/product';
import { ProductServiceService } from '../service/product-service.service';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent implements OnInit {

  list:Product;
  id;

  constructor(private product_service:ProductServiceService) { }

  ngOnInit(): void {
    this.product_service.getProductList().subscribe(data =>{
      this.list = data;
    })
  }

  onSelect(item){
    this.id = item
    console.log(this.id);
  }

}
