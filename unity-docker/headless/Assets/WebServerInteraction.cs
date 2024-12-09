using UnityEngine;
using System.Net.Http;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;

public class WebServerInteraction : MonoBehaviour
{
    private static readonly HttpClient client = new HttpClient();
    private const string WebServerUrl = "http://web_server:5000/should_render"; // Web Server URL
    private const string StreamerHost = "streamer_container";  // Streamer container hostname
    private const int StreamerPort = 12346; // Streamer container port

    async void Start()
    {
        try
        {
            // Make an HTTP GET request to the Web Server
            string response = await client.GetStringAsync(WebServerUrl);

            // Log the response from the Web Server
            Debug.Log("Web Server Response: " + response);

            // Decide what to send to the Streamer
            string message = response.Contains("\"render\":true") ? "Render graphics!" : "Do not render graphics.";
            System.IO.File.WriteAllText("/unity_project/render_decision.txt", message); // Save decision to a file

            // Send the decision to the Streamer
            SendToStreamer(message);
        }
        catch (System.Exception e)
        {
            Debug.LogError("Failed to connect to Web Server: " + e.Message);
        }
    }

    private void SendToStreamer(string message)
    {
        try
        {
            using (TcpClient client = new TcpClient(StreamerHost, StreamerPort))
            {
                byte[] data = Encoding.UTF8.GetBytes(message);
                NetworkStream stream = client.GetStream();
                stream.Write(data, 0, data.Length);
                Debug.Log("Message sent to Streamer: " + message);
            }
        }
        catch (System.Exception e)
        {
            Debug.LogError("Failed to send data to Streamer: " + e.Message);
        }
    }
}

