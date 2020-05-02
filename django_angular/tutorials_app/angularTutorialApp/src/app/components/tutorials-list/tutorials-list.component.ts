import { TutorialService } from './../../services/tutorial.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-tutorials-list',
  templateUrl: './tutorials-list.component.html',
  styleUrls: ['./tutorials-list.component.css']
})
export class TutorialsListComponent implements OnInit {

  tutorials:any;
  currentTutorial = null;

  constructor(private service:TutorialService) { }

  ngOnInit(): void {
    this.retrieveTutorials();
  }

  retrieveTutorials(){
    this.service.getAll().subscribe(data =>{
      this.tutorials = data;
      console.log(this.tutorials)
    },
    error => {
      console.log(error);
    })
  }

  setCurrentTutorial(tutorial){
    this.currentTutorial = tutorial;
    console.log(this.currentTutorial)
  }



}
