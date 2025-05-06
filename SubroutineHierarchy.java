import java.awt.*;
import java.awt.geom.AffineTransform;
import javax.swing.*;

public class SubroutineHierarchy extends JPanel {
    private double angle = 0;
    private boolean running = false;
    private Timer timer;

    public static void main(String[] args) {
        JFrame frame = new JFrame("Subroutinowa Scena z Animacją");
        SubroutineHierarchy panel = new SubroutineHierarchy();

        JButton toggleButton = new JButton("Run animation");
        toggleButton.addActionListener(e -> panel.toggleAnimation(toggleButton));

        JPanel topPanel = new JPanel(new FlowLayout(FlowLayout.LEFT));
        topPanel.add(toggleButton);

        frame.setLayout(new BorderLayout());
        frame.add(topPanel, BorderLayout.NORTH);
        frame.add(panel, BorderLayout.CENTER);

        frame.setSize(800, 600);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }

    private void toggleAnimation(JButton button) {
        if (!running) {
            running = true;
            button.setText("Stop animation");
            timer = new Timer(16, e -> {
                angle += 0.01;
                repaint();
            });
            timer.start();
        } else {
            running = false;
            button.setText("Run animation");
            if (timer != null) timer.stop();
        }
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2 = (Graphics2D) g;

        drawSeesaw(g2, 150, 200, 1.0, Color.MAGENTA);
        drawSeesaw(g2, 500, 400, 1.5, Color.BLUE);
        drawSeesaw(g2, 550, 100, 0.7, Color.GREEN);
    }

    private void drawSeesaw(Graphics2D g2, int x, int y, double scale, Color baseColor) {
        AffineTransform old = g2.getTransform();
        g2.translate(x, y);
        g2.scale(scale, scale);

        drawBase(g2, baseColor);
        drawBeam(g2);
        drawWheels(g2);

        g2.setTransform(old);
    }

    private void drawBase(Graphics2D g2, Color color) {
        g2.setColor(color);
        Polygon triangle = new Polygon();
        triangle.addPoint(0, 0);
        triangle.addPoint(-20, 100);
        triangle.addPoint(20, 100);
        g2.fill(triangle);
    }

    private void drawBeam(Graphics2D g2) {
        g2.setColor(Color.RED);
        g2.rotate(-0.3);  // Stałe nachylenie
        g2.fillRect(-100, -10, 200, 20);
    }

    private void drawWheels(Graphics2D g2) {
        g2.setColor(Color.BLACK);
        drawRotatingWheel(g2, -100, 0);
        drawRotatingWheel(g2, 100, 0);
    }

    private void drawRotatingWheel(Graphics2D g2, int offsetX, int offsetY) {
        AffineTransform old = g2.getTransform();
        g2.translate(offsetX, offsetY);
        g2.rotate(angle);
        g2.drawOval(-40, -40, 80, 80); // Średnica 80

        for (int i = 0; i < 12; i++) {
            double theta = i * Math.PI / 6;
            int x1 = (int) (Math.cos(theta) * 40);
            int y1 = (int) (Math.sin(theta) * 40);
            g2.drawLine(0, 0, x1, y1);
        }

        g2.setTransform(old);
    }
}
