import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProductServiceService {

  constructor(private http:HttpClient) { }

  getProductList(){
    return this.http.get('https://jsonplaceholder.typicode.com/albums');
  }

  getProductDetail(id:number){
    return this.http.get(`https://jsonplaceholder.typicode.com/albums/${id}`);
  }
}
