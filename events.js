

function CodeCheck(props){
    return <><div id="myDiv" >
            <input id="myInput" onChange={()=>{
                props.coupons.map(item=>{
                    if (myInput.value==item.code){
                        myImg.src=item.pic;
                    } else {
                        myImg.src="";
                    }
                })
            }}/>
        </div>
        <img src="" alt="" id="myImg" style={{"width":"100px"}}/>
        <div id="display">Result</div>
        </>
}

function StreetCheck(props){
    return <div id="myDiv">
        <input id="myInput" onChange={()=>{
            props.streets.includes(myInput.value)?myDiv.style.backgroundColor="green":myDiv.style.backgroundColor="red"
        }}/>
    </div>

}

function PhoneValidator(){
    const pattern=/0[5-7]\d-\d{6}/g;
    return <input id="phoneNumber" onChange={()=>{
        pattern.test(phoneNumber.value)?phoneNumber.style.backgroundColor="green":phoneNumber.style.backgroundColor="red";
    }}/>
}

function Todos(props){
    return <div>
        {props.todos.map((item)=>
            {if (item.completed=="yes"){
                <div style={{"backgroundColor":"blue"}}>{ item.name }</div>
            } else {
                <div style={{"backgroundColor":"red"}}>{ item.name }</div>
            }
        })
        }
        
        <div> { props.todos.length }</div>
    </div>
}

function IsBigger(prop){
    return <div>
        {prop.num>100?<div>is bigger</div>:<div>is smaller</div>}
    </div>
}

const root = ReactDOM.createRoot(document.getElementById("root"))

root.render(<Todos todos={
    [
        {name:"walk the dog", date: new Date("2023-08-01"), completed:"yes"}, 
        {name:"clean the house", date: new Date("2023-10-01"), completed:"no"}, 
    ]
}/>)

// root.render(<IsBigger num={99}/>)
