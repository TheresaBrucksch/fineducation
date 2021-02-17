var currentQuestionNo = 0;
var points = 0;
var rightAnswerPoints = 10;
var currentQuestion;

var questions = [
  {
    "id":"1",
    "question" : "Wofuer steht ueberhaupt der Begriff ETF?",
    "answers" : {
      "A":"Equity Traded Finance",
      "B":"Equity Traded Fond",
      "C":"Energy Trade Fond ",
      "D":"Effective Trading Floor"
    }, 
    "right":"B"
  },{
    "id":"2",
    "question" : "Wie viel Dollar schaetzt du, verwaltet der groesste ETF der Welt (September 2020)?",
    "answers" : {
      "A":"$ 278.000.000 ",
      "B":"$ 2.780.000.000.000 ",
      "C":"$ 2.780.000.000 ",
      "D":"$ 278.000.000.000 "
    }, 
    "right":"D"
  }
];

function showNextQuestion() {
  if (currentQuestionNo >= questions.length) {
    showEnd();
    currentQuestionNo = 0;
  }
  console.log("Loading Question:" + currentQuestionNo);
  currentQuestion = questions[currentQuestionNo];
  $("#qno").text(currentQuestionNo+1);
  $("#question_text").text(currentQuestion.question);
  $("#answer_a").text(currentQuestion.answers.A);
  $("#answer_b").text(currentQuestion.answers.B);
  $("#answer_c").text(currentQuestion.answers.C);
  $("#answer_d").text(currentQuestion.answers.D); 
  
  $(".answer").removeClass("btn-primary btn-danger btn-success btn-default");
  $(".answer").addClass("btn-default");
}

function getRightAnswer() {
  return currentQuestion.right;
}