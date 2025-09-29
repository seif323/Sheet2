"use strict";
const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split("\n");
const n = Number(input[0]);

for(let i =1; i<=n ;i++){
    if (n % i === 0){
        console.log(i);
    }
}