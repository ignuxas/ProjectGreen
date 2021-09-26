var AllCon = 0;
intID = 1;

ItemTable = document.getElementById("ItemTable");

document.getElementById("checkBtn").addEventListener("click", ()=>{ // when apply button clicked

	//get values of settings
	searchword = document.getElementById("search").value; console.log(searchword); 
	pages = document.getElementById("Pages").value;
	rtime = document.getElementById("RTime").value;
	namesearch = document.getElementById("NameSearch").value;
	showdesc = document.getElementById("showdesc").checked;
	notif = document.getElementById("notify").checked;

	console.log(showdesc)

	if (searchword == ""){
		document.getElementById("search").style.borderColor="red" //make url bar red if empty
	} else{
		document.getElementById("search").style.borderColor="#fff"
	}

	if (pages == ""){
		document.getElementById("Pages").style.borderColor="red" //make pages bar red if empty
	} else{
		document.getElementById("Pages").style.borderColor="#fff"
	}

	//timer function: (if I did this in Python it would be slow and sometimes the UI does not work if you do it in Python)
	//skelbiu
	if (rtime != ""){
		if (rtime < 5){rtime = 5}
		clearInterval(intID);
		eel.skelbiu(searchword, pages, rtime)
		const intervalId = setInterval(function(){eel.skelbiu(searchword, pages, notif)}, rtime * 1000); //activate python scrape function with timer
		intID+=1;
		console.log(intervalId, intID)}
	else{eel.skelbiu(searchword, pages, notif); clearInterval(intID);}; //activate python scrape function
	//autoplius
	if(searchword.search('autoplius.lt') != -1){
		if (rtime != ""){
			if (rtime < 5){rtime = 5}
			clearInterval(intID);
			eel.autoplius(searchword, pages, rtime)
			const intervalId = setInterval(function(){eel.autoplius(searchword, pages, notif)}, rtime * 1000); //activate python scrape function with timer
			intID+=1;
			console.log(intervalId, intID)}
			else{eel.autoplius(searchword, pages, notif); clearInterval(intID);}; //activate python scrape function
		}
	}, false);
	
ItemTable = document.getElementById("ItemTable");

eel.expose(CleanTable)
function CleanTable() {
	while (ItemTable.firstChild) {ItemTable.removeChild(ItemTable.lastChild);} //while there is something in table delete a child
}

eel.expose(UpdateTableSkelbiu)
function UpdateTableSkelbiu(url, price, time, city, condition, name, description, itemnum) {
	//pretty unoptimized but works ¯\_(ツ)_/¯
	//everything is in a span cause its easier to color if color function were to be added (just like el_spanName)

	//price
	el_spanPrice = document.createElement('span');
	addprice = document.createTextNode(price);
	el_spanPrice.appendChild(addprice);
	//time
	el_spanTime = document.createElement('span');
	el_spanTime.className = "time";
	addtime = document.createTextNode(time);
	//city
	el_spanCity = document.createElement('span');
	el_spanCity.className = "city";
	addcity = document.createTextNode(city);
	//condition
	el_spanCondition = document.createElement('span');
	el_spanCondition.className = "condition";
	addcondition = document.createTextNode(condition);
	//name
	el_spanName = document.createElement('span');
	el_spanName.className = "name";
	if(namesearch.length != 0){if(name.toUpperCase().search(namesearch.toUpperCase()) != -1){el_spanName.setAttribute('style', 'color: green')};};
	addname = document.createTextNode(name);
	//description
	if(showdesc == true){
		el_spanDescription = document.createElement('span');
		el_spanDescription.className = "description";
		adddescription = document.createTextNode(description);
		el_spanDescription.setAttribute('style', 'color: #858585')
	}

 	creatediv = document.createElement('div')
	a1 = document.createElement("a");
  	ItemTable.appendChild(creatediv);
  	creatediv.classList.add("listitem");
  	creatediv.appendChild(a1);

  	a1.setAttribute("href", url); // set url on item
  	a1.setAttribute('target', "_blank"); // make it so the url opens in new tab, if browser is closed open browser and open tab
  	a1.appendChild(el_spanPrice);
  	a1.appendChild(el_spanTime);
  	a1.appendChild(el_spanCity);
  	a1.appendChild(el_spanCondition);
  	a1.appendChild(el_spanName);
  	if(showdesc == true){a1.appendChild(el_spanDescription);}

  	document.getElementsByClassName('time')[itemnum].appendChild(addtime);
  	document.getElementsByClassName('city')[itemnum].appendChild(addcity);
  	document.getElementsByClassName('condition')[itemnum].appendChild(addcondition);
  	document.getElementsByClassName('name')[itemnum].appendChild(addname);
  	if(showdesc == true){document.getElementsByClassName('description')[itemnum].appendChild(adddescription);}
};

eel.expose(UpdateTableAutoplius)
function UpdateTableAutoplius(url, price, year, name, parameters, itemnum) {
	//pretty unoptimized but works ¯\_(ツ)_/¯
	//everything is in a span cause its easier to color if color function were to be added (just like el_spanName)

	//price
	el_spanPrice = document.createElement('span');
	addprice = document.createTextNode(price);
	el_spanPrice.appendChild(addprice);
	//year
	el_spanYear = document.createElement('span');
	el_spanYear.className = "year";
	addyear = document.createTextNode(year);
	//name
	el_spanName = document.createElement('span');
	el_spanName.className = "name";
	addname = document.createTextNode(name);
	//parameters
	if(showdesc == true){
		el_spanParameters = document.createElement('span');
		el_spanParameters.className = "parameters";
		if(namesearch.length != 0){if(parameters.toUpperCase().search(namesearch.toUpperCase()) != -1){el_spanParameters.setAttribute('style', 'color: green')};};
		addparameters = document.createTextNode(parameters);
	}

 	creatediv = document.createElement('div')
	a1 = document.createElement("a");
  	ItemTable.appendChild(creatediv);
  	creatediv.classList.add("listitem");
  	creatediv.appendChild(a1);

  	a1.setAttribute("href", url); // set url on item
  	a1.setAttribute('target', "_blank"); // make it so the url opens in new tab, if browser is closed open browser and open tab
  	a1.appendChild(el_spanPrice);
  	a1.appendChild(el_spanYear);
  	a1.appendChild(el_spanName);
  	if(showdesc == true){a1.appendChild(el_spanParameters);}

  	document.getElementsByClassName('year')[itemnum].appendChild(addyear);
  	document.getElementsByClassName('name')[itemnum].appendChild(addname);
  	if(showdesc == true){document.getElementsByClassName('parameters')[itemnum].appendChild(addparameters);}
};
