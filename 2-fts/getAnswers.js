const request = require('request');
const fs = require('fs');
const base_url = "http://localhost:9200/"
const index_name = process.argv[2];
const exec = require('child_process').exec;


const make_request = (file_path, func_path, callback)=>{
    fs.readFile(file_path, "utf8", (err, data)=>{
        const payload = JSON.parse(data);
        request.post(base_url + index_name + func_path, {json: true, body: payload}, (err, res, body)=>{
            callback(body);
        });
    });
}

make_request("./countSzkoda.json", "/_count", (body)=>{
    console.log("6. Orzeczeń ze słowem \"szkoda\": " + body.count);
    make_request("./countUszczerbek.json", "/_count", (body)=>{
        console.log("7. Orzeczeń z \"trwałym uszczerbkiem na zdrowiu\": " + body.count);
        make_request("./countUszczerbek2.json", "/_count", (body)=>{
            console.log("8. Orzeczeń z \"trwałym uszczerbkiem na zdrowiu\" z max. 2 wyrazową przerwą: " + body.count);
            make_request("./mostJudges.json", "/_search", (body)=>{
                console.log("9. Sędziowie z największą liczbą orzeczeń:");
                body.aggregations.top_judges.buckets.forEach((el, i)=>{console.log("\t" + (i + 1) + ") " + el.key + ": " + el.doc_count)});
                make_request("./dateHistogram.json", "/_search", (body)=>{
                    const judgments = new Array(12).fill(0);
                    body.aggregations.judgments.buckets.forEach((elem)=>{
                        judgments[Number(elem.key_as_string.substr(5,2))-1] = elem.doc_count;
                    });
                    
                    const str_to_write = judgments.map((amount, index)=>(index + 1) + ", " + amount).join("\n");

                    fs.writeFile("histogramData.txt", str_to_write, ()=>{
                        exec("gnuplot histogramPlot.gpi");
                    });
                    
                });
            });
        })
    })
});
