package edu.coursera.distributed;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;

public final class FileServer {

    public void run(final ServerSocket socket, final PCDPFilesystem fs,
            final int ncores) throws IOException {

        while (true) {
            final Socket client = socket.accept();

            Thread worker = new Thread(new Runnable() {
                @Override
                public void run() {
                    try {
                        handleClient(client, fs);
                    } catch (IOException e) {
                        // Ignore individual client errors.
                    } finally {
                        try {
                            client.close();
                        } catch (IOException e) {
                            // Ignore close errors.
                        }
                    }
                }
            });

            worker.start();
        }
    }

    private void handleClient(final Socket client,
            final PCDPFilesystem fs) throws IOException {

        InputStream input = client.getInputStream();
        OutputStream output = client.getOutputStream();

        StringBuilder request = new StringBuilder();
        int previous = -1;
        int current;

        while ((current = input.read()) != -1) {
            request.append((char) current);

            if (previous == '\r' && current == '\n') {
                if (request.length() >= 4
                        && request.substring(request.length() - 4)
                                .equals("\r\n\r\n")) {
                    break;
                }
            }

            previous = current;
        }

        String[] lines = request.toString().split("\r\n");

        if (lines.length == 0) {
            return;
        }

        String[] parts = lines[0].split(" ");

        if (parts.length < 2 || !"GET".equals(parts[0])) {
            return;
        }

        String path = parts[1];

        PCDPPath filePath = new PCDPPath(path);

        String contents = fs.readFile(filePath);

        if (contents != null) {
            String header = "HTTP/1.0 200 OK\r\n"
                    + "Server: FileServer\r\n"
                    + "\r\n";

            output.write(header.getBytes());
            output.write(contents.getBytes());
        } else {
            String header = "HTTP/1.0 404 Not Found\r\n"
                    + "Server: FileServer\r\n"
                    + "\r\n";

            output.write(header.getBytes());
        }

        output.flush();
    }
}