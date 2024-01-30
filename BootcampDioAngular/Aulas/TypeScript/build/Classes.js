"use strict";
//classes
var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
/*
  data modifiers
  public
  private
  protected
*/
var Character = /** @class */ (function () {
    function Character(name, stregth, skill) {
        this.name = name;
        this.stregth = stregth;
        this.skill = skill;
    }
    Character.prototype.attack = function () {
        console.log("Attack with ".concat(this.stregth, " points"));
    };
    return Character;
}());
//Character: superclass
//Magician: subclass
var Magician = /** @class */ (function (_super) {
    __extends(Magician, _super);
    function Magician(name, stregth, skill, magicPoints) {
        var _this = _super.call(this, name, stregth, skill) || this;
        _this.magicPoints = magicPoints;
        return _this;
    }
    return Magician;
}(Character));
var p1 = new Character("Ryu", 10, 98);
var p2 = new Magician("Mago", 9, 30, 100);
p1.skill = 12;
