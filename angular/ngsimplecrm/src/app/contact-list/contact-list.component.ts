import { Component, OnInit } from '@angular/core';
import { ContactService } from '../service/contact.service';

@Component({
  selector: 'app-contact-list',
  templateUrl: './contact-list.component.html',
  styleUrls: ['./contact-list.component.css']
})
export class ContactListComponent implements OnInit {

  displayedColumns : string[] = ['id', 'first_name', 'last_name', 'email', 'phone', 'account', 'address', 'description', 'createdBy', 'createdAt', 'isActive', 'actions'];
  dataSource = [];

  constructor(private contactService: ContactService) { }

  ngOnInit(): void {
    this.fetchContacts();
  }

  fetchContacts(){
    this.contactService.getFirstPage().subscribe((data: Array<object>) => {
    this.dataSource = data;
    console.log(data);
    });
    }

}
