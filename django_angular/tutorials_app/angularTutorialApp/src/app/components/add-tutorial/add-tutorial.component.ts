import { TutorialService } from './../../services/tutorial.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-add-tutorial',
  templateUrl: './add-tutorial.component.html',
  styleUrls: ['./add-tutorial.component.css']
})
export class AddTutorialComponent implements OnInit {

  tutorial = {
    'title':'',
    'description':'',
    'published':false
  }
  submitted:boolean = false

  constructor(private service:TutorialService) { }

  ngOnInit(): void {
  }

  saveTutorial(){
    console.log(this.tutorial)
    this.service.create(this.tutorial).subscribe(response => {
      console.log(response);
      this.submitted = true
    },
    error => {
      console.log(error)
    }
    )
  }

  newTutorial(){
      this.submitted = false
      this.tutorial = {
        'title':'',
        'description':'',
        'published':false
      }
  }



}
