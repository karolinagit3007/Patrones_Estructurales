package dispositivos;

abstract class Dispositivo {
    public abstract void encender();
    public abstract void apagar();
    public abstract void setVolume(int volume);
}

class Televisor extends Dispositivo {
    private int volume;

    public Televisor() {
        this.volume = 0;
    }

    @Override
    public void encender() {
        System.out.println("Televisor encendido");
    }

    @Override
    public void apagar() {
        System.out.println("Televisor apagado");
    }

    @Override
    public void setVolume(int volume) {
        this.volume = volume;
        System.out.println("Volumen: " + this.volume);
    }
}

class Radio extends Dispositivo {
    private int volume;

    public Radio() {
        this.volume = 5;
    }

    @Override
    public void encender() {
        System.out.println("Radio encendido");
    }

    @Override
    public void apagar() {
        System.out.println("Radio apagado");
    }

    @Override
    public void setVolume(int volume) {
        this.volume = volume;
        System.out.println("Volumen: " + this.volume);
    }
}

public class Builder {
    public static void main(String[] args) {
        Televisor televisor = new Televisor();
        Radio radio = new Radio();

        televisor.encender();
        televisor.setVolume(15);
        televisor.apagar();

        radio.encender();
        radio.setVolume(10);
        radio.apagar();
    }
}
