const request = require('request');
const sync_request = require('sync-request');
const syncrequest = require('syncrequest');
const fs = require('fs');
const base_url = "http://localhost:9200/"
const index_name = process.argv[2];
const database_path = process.argv.length < 4 ? "/home/mariusz/Pobrane/data/json/" : process.argv[3];

const firstWith2014 = 1011;
const lastWith2014 = 1572;
//const lastWith2014 = 1100;

//mixed synchronous and asynchronous way. full asynchronous was crashing garbage collector with this amount of data

fs.readFile("./createIndex.json", "utf8", (err, data)=>{
    const createIndex = JSON.parse(data);
    request.put(base_url + index_name, {json: true, body: createIndex}, (err, res, body)=>{
        let id = 0;
        for(let judgmentFileIndex = firstWith2014; judgmentFileIndex < lastWith2014; ++judgmentFileIndex)
        {
            console.log(judgmentFileIndex);
            const dataFile = fs.readFileSync(database_path + "judgments-" + judgmentFileIndex + ".json", "utf8");
            const judgmentsJson = JSON.parse(dataFile);
            judgmentsJson.items.forEach((item)=>{
                if(item.judgmentDate.substr(0,4) == "2014")
                {
                    const judgmentBodyToSend = {
                        judgmentText: item.textContent,
                        judgmentDate: item.judgmentDate,
                        judges: item.judges.map(judge=>judge.name),
                        signature: item.id
                    };
                    sync_request("PUT", base_url + index_name + "/doc/" + id + "/_create", {json: judgmentBodyToSend});
                    ++id;
                }
            });
        }
    });
});
