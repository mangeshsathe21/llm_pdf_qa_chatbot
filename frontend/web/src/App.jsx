import { useState } from 'react'
import { styled } from '@mui/material/styles'
import './App.css'
import Box from '@mui/material/Box'
import Select from '@mui/material/Select'
import FormControl from '@mui/material/FormControl'
import MenuItem from '@mui/material/MenuItem'
import InputLabel from '@mui/material/InputLabel'
import axios from "axios"
import { useEffect } from 'react'
import TextareaAutosize from '@mui/material/TextareaAutosize'
import Button from '@mui/material/Button'

function App() {

  const [document, setDocument] = useState('')
  const [uploadFolderDocs, pullUploadDirectory] = useState([])
  const [askQuery, setAskQuery] = useState('')
  const [llmResponse, setLlmResponse] = useState('')
  useEffect(() =>{
    const fetchDocumentList = async () => {
         try{
                const apiClient = axios.create({baseURL : 'http://127.0.0.1:8001/listdocument'})
                const response = await apiClient.get()
                pullUploadDirectory(response.data.documents)              
            } 
            catch(error){
              console.log('Error : '+ error) 
            }
            finally{
              console.log('finally')
            }
    }
    fetchDocumentList()
  },[]);


  const handlePostQuery = async () => {
    
    try{
      const api_client = axios.create()
      const response = await api_client.post('http://127.0.0.1:8001/ask', {
        'documentname' : document,
        'documentask' : askQuery
      })
      console.log(response.data)
      setLlmResponse(response.data.llmresponse)
    }
    catch (error) {
      console.log("ERROR" + error)
    }
    finally{
      console.log('FINALLY')
    }
  };

 

  return (
    <>
     <Box sx={{
      margin: '5% auto',
      padding: '10px',
      backgroundColor:'#c2cadaff',
      borderRadius: "5px",
      maxWidth: 800,
      fontSize: 18
     }}>
          Built a local LLM PDF Q&A chatbot <strong>(React, FastAPI, LangChain, Ollama, ChromaDB)</strong> enabling source-cited document search with zero external API dependency.
          <Box sx={{
            margin: '1% auto',
            padding: '10px',
            backgroundColor: '#f5d056ff',
            borderRadius: '5px',
            height: 'auto'
          }}>
              <FormControl fullWidth>
                <InputLabel id="document-id" >LLM Document</InputLabel>
                <Select 
                labelId='document-id'
                id='documentselect-id'
                value={document}
                onChange={(event) => setDocument(event.target.value)}
                label='Select lable'>
                  {uploadFolderDocs.map((item) => (
                    <MenuItem key={item} value={item}>{item}</MenuItem>
                  ))}
                </Select>
                
              </FormControl>

              <FormControl sx={{margin: '2% auto'}} fullWidth>

                <TextareaAutosize 
                id="ask-id" 
                label='Ask' 
                variant='outlined' 
                minRows={3} 
                placeholder='Select the document and ask the query'
                value = {askQuery}
                onChange={(event) => {setAskQuery(event.target.value)}}
                sx={{
                  width:200, 
                  backgroundColor:"#e0e0ddff",
                  resize:'none'}}>

                </TextareaAutosize>
              </FormControl>

              <FormControl sx={{margin: '2% auto', alignItems:'center'}} >
                <Button 
                  id="post-query-id" 
                  label="Post Query" 
                  variant='outlined' 
                  onClick={handlePostQuery}
                  sx ={{
                    backgroundColor : '#ffffff',
                    borderColor: '#1b45fdff',
                  }}
                  >
                    POST QUERY
                  </Button>
              </FormControl>

          </Box>
          Response from LLM (Ollama 3.1)
          <Box sx={{
            margin: '1% auto',
            padding: '10px',
            backgroundColor: '#f5d056ff',
            borderRadius: '5px',
            height: 'auto'
          }}>
            <div>{llmResponse}</div>
          </Box>
     </Box>
     
    </>
  )
}

export default App
