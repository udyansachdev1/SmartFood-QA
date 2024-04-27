use actix_web::{web, App, HttpResponse, HttpServer, Responder};
use anyhow::Error;
use reqwest;
use serde_json::{json, Value}; // Import the Error type from the anyhow crate

const API_URL: &str =
    "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct";
const BEARER_TOKEN: &str = "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";

async fn query(payload: Value) -> Result<Value, Error> {
    let client = reqwest::Client::new();
    let response = client
        .post(API_URL)
        .header("Authorization", format!("Bearer {}", BEARER_TOKEN))
        .json(&payload)
        .send()
        .await?;

    // Check if response is successful
    if response.status().is_success() {
        let body = response.text().await?;
        let json_body: Value = serde_json::from_str(&body)?;
        Ok(json_body)
    } else {
        // Convert anyhow::Error to Box<dyn std::error::Error>
        Err(Error::from(anyhow::anyhow!(
            "Request failed with status: {}",
            response.status()
        )))
    }
}

async fn handle_query(json_payload: web::Json<Value>) -> impl Responder {
    match query(json_payload.into_inner()).await {
        Ok(result) => HttpResponse::Ok().json(result),
        Err(err) => HttpResponse::InternalServerError().body(format!("Error: {:?}", err)),
    }
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| App::new().route("/query", web::post().to(handle_query)))
        .bind("127.0.0.1:8080")?
        .run()
        .await
}
