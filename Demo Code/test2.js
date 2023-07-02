var i=0;
var p = [];
for(j=0;j<=100;j++){
    i=i+1;
    if(i%2==0 && i%3==0){
        p.push(i);
    }
}
console.log(p.sort(function(a, b){return a-b})[3]);