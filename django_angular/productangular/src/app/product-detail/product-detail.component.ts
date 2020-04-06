import { Component, OnInit, Input } from '@angular/core';
import { ProductServiceService } from '../service/product-service.service';

@Component({
  selector: 'app-product-detail',
  templateUrl: './product-detail.component.html',
  styleUrls: ['./product-detail.component.css']
})
export class ProductDetailComponent implements OnInit {

  @Input() id;
  product:Object;

  constructor(private service:ProductServiceService) { }

  ngOnInit(): void {
    console.log(this.id);
  }

}
