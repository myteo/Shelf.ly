/**
 * Created by leonmak on 21/10/17.
 * View controller for watch
 */

import document from "document";

var notificationLbl = document.getElementById("notification");
var notificationSubLbl = document.getElementById("notification-subtitle");

var buyButton = document.getElementById("buy-button");
var cardImage = document.getElementById("card-image");
var shoeImage = document.getElementById("shoe-image");
var socksImage = document.getElementById("socks-image");
var noBtn = document.getElementById("btn-no");
var yesBtn = document.getElementById("btn-yes");

function didInit() {
    buyButton.style.display = "none"
    shoeImage.style.display = "none"
    cardImage.style.display = "none"
    socksImage.style.display = "none"
    noBtn.style.display = "none"
    yesBtn.style.display = "none"  

    setTimeout(function() {
        toggle(buyButton)
        toggle(shoeImage)
        setText("Nike Flex US 11", notificationLbl);
        setText("is in stock", notificationSubLbl)
    }, 1000)  
}

function setText(text, label) {
    label.innerText = text
}

function toggle(ele) {
    ele.style.display = (ele.style.display === "inline") ? "none" : "inline";
}


function togglePromos() {
    toggle(yesBtn)
    toggle(noBtn)  
}

buyButton.onactivate = function(evt) {
    console.log("Activate promo!");
    buyButton.style.display = "none"
    toggle(shoeImage)
    toggle(socksImage)
    togglePromos()
    var transactionHandler = function (evt) {
        console.log("Activate payment!");
        toggle(socksImage)   
        togglePromos()

        toggle(cardImage)
        cardImage.onclick = function(evt) {
          toggle(cardImage)
            setText("Transaction Completed", notificationLbl);
            setText("0 items in watchlist", notificationSubLbl)
        }
    }
  
    noBtn.onclick = transactionHandler
    yesBtn.onclick = transactionHandler
    socksImage.onclick = transactionHandler
}


didInit()

