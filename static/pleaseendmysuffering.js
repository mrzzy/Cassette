function closeNav() {
  document.getElementById("legendSideBar").style.width = "0";
  
}

function openNav() {
  document.getElementById("legendSideBar").style.width = "200px";
  $(document).mouseup(function(e) 
    {
        var container = $("legendSideBar");

        // if the target of the click isn't the container nor a descendant of the container
        if (!container.is(e.target) && container.has(e.target).length === 0) 
        {
            closeNav();
        }
    });
}

function deleteDivs() {
  document.getElementById("bigContainer").innerHTML = "";
}

function showTrashcan() {
  document.getElementById("deleteBtn").style.display = "block";
}

window.addEventListener("load",function() {
    setTimeout(function(){
        // This hides the address bar:
        window.scrollTo(0, 1);
    }, 0);
});
