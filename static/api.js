
function TaskBoard(){
    const [tasksNum, setTasksNum]=React.useState([]);
    React.useEffect(()=>{
        axios.get('/api/tasks_board').then((response)=>{
            setTasksNum(response.data.length)
        })
    },[]
    );
    return <div>Tasks<br/>{tasksNum}</div>   
}


const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<TaskBoard/>);


