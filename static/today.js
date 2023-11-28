
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

const tasks_board = ReactDOM.createRoot(document.getElementById("tasks_board"));
tasks_board.render(<TaskBoard/>);


