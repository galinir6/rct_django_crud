import axios from 'axios'
import React, { useEffect, useState } from 'react'

function App() {

  const SERVER = " http://127.0.0.1:8000/products"

  const [name, setname] = useState("")
  const [price, setprice] = useState(0)
  const [cat, setcat] = useState("")
  const [prods, setprods] = useState([])
  const [refFlag, setrefFlag] = useState(true)

  const add = () => {
    axios.post(SERVER, { "name": name, "price": price, "category": cat }).then(res => setrefFlag(! refFlag))
  }

  useEffect(() => {
        axios.get(SERVER).then(res => setprods(res.data))
    }, [refFlag])


  const upd = (id) => {
    axios.put(`${SERVER}/${id}`, { "name": name, "price": price, "category": cat }).then(res => setrefFlag(! refFlag))
  }

  const del = (id) => {
    axios.delete(`${SERVER}/${id}`).then(res => setrefFlag(! refFlag))
  }

  return (
    <div>
      <h1>Products CRUD with django server</h1><br />

      Add product:
      Name: <input onChange={(e) => setname(e.target.value)}></input>
      Price: <input onChange={(e) => setprice(e.target.value)} type='number'></input>
      Category: <input onChange={(e) => setcat(e.target.value)}></input>
      <button onClick={() => add()}>Add</button><br /><br />
     
      <h3>total items: {prods.length}</h3><br />

      <div className="row row-cols-1 row-cols-md-6 g-4">
        {prods.map((product, ind) =>
          <div key={ind} className="col">
            <div className="card">
              <img src={`https://picsum.photos/10${ind}`} alt='img' className='card-img-top' />
              <div className="card-body">
                <h5 className="card-title">product: {product.name}</h5>
                <p className="card-text">price: {product.price}</p>
                <p className="card-text">category: {product.category}</p>
                <button className='btn btn-success'>buy</button>
                <button className='btn btn-danger' onClick={() => del(product.id)}>remove</button>
                <button className='btn btn-warning' onClick={() => upd(product.id)}>update</button>

              </div>
            </div>
          </div>)}
      </div>
    </div>
  );
}
export default App;
