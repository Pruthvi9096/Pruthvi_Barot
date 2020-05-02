import { TutorialService } from './../../services/tutorial.service';
import { Component, OnInit, Input } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-tutorial-details',
  templateUrl: './tutorial-details.component.html',
  styleUrls: ['./tutorial-details.component.css']
})
export class TutorialDetailsComponent implements OnInit {

  @Input() tutorial:any;
  tutorialData:any;

  constructor(private route:ActivatedRoute,private service:TutorialService,private router:Router) { }

  ngOnInit(): void {
    if(!this.tutorial){
      console.log(this.route.snapshot.paramMap.get('id'))
      this.service.get(this.route.snapshot.paramMap.get('id')).subscribe(response =>{
        console.log(response);
        this.tutorialData  = response;
      },
      error => {
        console.log(error);
      })
    }
  }

  publishTutorial(tutorial){
    tutorial.published = !tutorial.published;
  }

  updateTutorial(tutorial){
    this.service.update(tutorial.id,tutorial).subscribe(
      response => {
        console.log(response);
        // this.router.navigate(['/']);  
      },
      error => {
        console.log(error);
      })

  }

  deleteTutorial(id){
    this.service.delete(id).subscribe(
      response => {
        console.log(response);
        
      },
      error => {
        console.log(error);
        
      }
    )
  }

}
