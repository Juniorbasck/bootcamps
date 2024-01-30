"use strict";
var bot1 = {
    id: "1",
    name: "megaman",
};
var bot2 = {
    id: "1",
    name: "megaman",
    sayHello: function () {
        throw new Error("Function not implemented.");
    },
};
var Pessoa = /** @class */ (function () {
    function Pessoa(id, name) {
        this.id = id;
        this.name = name;
    }
    Pessoa.prototype.sayHello = function () {
        return "hello i'm ".concat(this.name);
    };
    return Pessoa;
}());
var p = new Pessoa(1, "gutsman");
console.log(p.sayHello());
