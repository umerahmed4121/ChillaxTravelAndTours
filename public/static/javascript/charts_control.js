let chart_selected=false



// checks weather the chart is selected or not 
// and also adds the heading for the selected chart
function selected_chart_checker(chart_heading) {
    if (!chart_selected){
        document.querySelector(".popup_chart_container").remove()
        return
    }
    
    // if (chart_selected){
    let popup_chart_container=document.createElement('div')
    popup_chart_container.innerHTML=`
        <button onclick="event_handler_chart_close()">close</button>
        <h2>Chart for</h2>
        <p>${chart_heading}</p>
        <canvas id="myChart"></canvas>`
    popup_chart_container.classList.add("popup_chart_container")
    document.querySelector(".container").appendChild(popup_chart_container)
    
}


function Chart_marker({data_title_arr,data_id_arr}) {
    const ctx = document.getElementById('myChart').getContext('2d');
    const myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels:data_id_arr,
        datasets: [{
            label: 'title length',
            data: data_title_arr,
            fill:true,
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor:'rgba(255, 99, 132, 1)',
            borderWidth: 2
        }]
        }

    });
    
}


async function data_fetcher(url) {
    console.log(url)
    const response=await fetch(url)
    const data=await response.json()
    console.log(data)
    data_title_arr=data.map((obj)=>obj.title.length)
    data_id_arr=data.map((obj)=>obj.id)
    const obj={data_title_arr:data_title_arr,data_id_arr:data_id_arr}
    Chart_marker(obj)
    console.log(obj)
}





function event_handler_chart_div(element) {
    let selected_chart_text=element.childNodes[5].innerText
    chart_selected=true
    // making chart 
    selected_chart_checker(selected_chart_text)

    // now depending upon the selected_chart_text diffeent data fetcher is going to be called 
    url = "https://jsonplaceholder.typicode.com/posts"
    if(selected_chart_text==="Total Users"){

        data_fetcher(url)
    }else if(selected_chart_text==="Total Packages"){
        data_fetcher(url)
    }else if(selected_chart_text==="Total Hotels"){
        data_fetcher(url)
    }else if(selected_chart_text==="Total Transports"){
        data_fetcher(url)
    }
}
function event_handler_chart_close() {
    chart_selected=false
    selected_chart_checker()
}



