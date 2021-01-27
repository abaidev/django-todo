'use strict';

const csrftoken = Cookies.get('csrftoken');

const get_todos = async () => {
    let todos = await fetch("/api/todo/")
        .then(res => res.json())
        .then(todos => {
            return todos
        });
    await console.log(todos);
    return todos;
};

const create_todo = async (todo) => {
    console.log("CREATING tODO", todo);
    await fetch("/api/todo/", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json;charset=utf-8',
            "X-CSRFToken": csrftoken,
        },
        body: JSON.stringify({
            "task": todo
        })
    });
};

const delete_todo = async (todoId) => {
    console.log("DELETING tODO", todoId);
    await fetch(`/api/todo/${todoId}/`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json;charset=utf-8',
            "X-CSRFToken": csrftoken,
        }
    });
};

const edit_todo = async (todoId, todo) => {
    await fetch(`/api/todo/${todoId}/`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json;charset=utf-8',
            "X-CSRFToken": csrftoken,
        },
        body: JSON.stringify({
            "task": todo
        })
    });
};

// TODO: ALL IN ONE
// const obt_todo = async({method = "GET", todoId = null, todo = null})=>{
//     let url = method === 'GET' || method === 'POST' ? "/api/todo/" : `/api/todo/${todoId}`;
//     await fetch(url, {
//         method: method,
//         headers: {
//             'Content-Type': 'application/json;charset=utf-8',
//             "X-CSRFToken": csrftoken,
//         },
//         body: JSON.stringify({
//             "task": todo
//         })
//     });
// };

const App = () => {
    const [todos, setTodos] = React.useState([]);
    const [newTodo, setNewTodo] = React.useState("");
    const [refresh, setRefresh] = React.useState(false);

    React.useEffect(()=>{
        let todos = get_todos();
        todos.then(data => setTodos(data.reverse()));
    }, [newTodo, refresh]);

    return (
        <div>
            <Dashboard addBtn={(val)=>{setNewTodo(val); create_todo(val)}}/>

            {todos.length > 0 && <div className="d-grid gap-3">
                {todos.map((item, ind)=>{
                    return <TaskItem item={item} key={ind+3} id={item.id} toRefresh={()=> setRefresh(!refresh)} />
                })}
            </div>}

        </div>
    )
};

const Dashboard = ({addBtn})=>{
    const [inpVal, setInpVal] = React.useState("");

    return(
        <div className="input-group mb-3">
            <input type="text" className="form-control" placeholder="Enter a task" onChange={(val)=>setInpVal(val.target.value)}/>
            <button className="btn btn-secondary" type="button" id="button-addon2" onClick={()=>addBtn(inpVal)}>Add</button>
        </div>
    )
};

const TaskItem = ({item, id, toRefresh})=>{
    const [edit, setEdit] = React.useState(false);
    const [inpVal, setInpVal] = React.useState(item.task);

    return (
        <div className="col border border-secondary border-2 p-2 rounded">
            <div className="row pe-2">

                <div className="col">
                    {edit && <div className="input-group">
                        <input type="text" className="form-control" placeholder="Edit a task"
                               onChange={(val) => setInpVal(val.target.value)} defaultValue={inpVal}/>
                        <button className="btn btn-outline-success" onClick={() => {edit_todo(id, inpVal); toRefresh(); setEdit(!edit)}}>Save</button>
                    </div>}

                    {!edit && <div>
                        <h5 className="title">{item.task}</h5>
                        <p className="h6">{new Date(item.created).toLocaleDateString()} {new Date(item.created).toLocaleTimeString()}</p>
                    </div>}
                </div>

                <div className="col-lg-1 col-1 p-3">
                    <button className="btn btn-primary" onClick={()=>{setEdit(!edit)}}>Edit</button>
                </div>

                <div className="col-lg-1 col-1 p-3">
                    <button className="btn btn-danger" onClick={()=>{delete_todo(id); toRefresh();}}>Delete</button>
                </div>

            </div>
        </div>
    )
};

ReactDOM.render(<App/>, document.getElementById('root'));