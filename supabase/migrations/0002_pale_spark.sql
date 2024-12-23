-- Create servers table
CREATE TABLE servidores (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    nombre text NOT NULL,
    dirip text NOT NULL
);

-- Create applications table
CREATE TABLE aplicaciones (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    nombre text NOT NULL,
    carpeta text NOT NULL,
    idservidor uuid REFERENCES servidores(id) ON DELETE CASCADE
);

-- Create files table
CREATE TABLE ficheros (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    nombre text NOT NULL,
    carpeta text NOT NULL,
    idservidor uuid REFERENCES servidores(id) ON DELETE CASCADE,
    idaplicacion uuid REFERENCES aplicaciones(id) ON DELETE CASCADE
);

-- Enable RLS
ALTER TABLE servidores ENABLE ROW LEVEL SECURITY;
ALTER TABLE aplicaciones ENABLE ROW LEVEL SECURITY;
ALTER TABLE ficheros ENABLE ROW LEVEL SECURITY;

-- Create policies
CREATE POLICY "Enable read access for all users" ON servidores FOR SELECT USING (true);
CREATE POLICY "Enable read access for all users" ON aplicaciones FOR SELECT USING (true);
CREATE POLICY "Enable read access for all users" ON ficheros FOR SELECT USING (true);

CREATE POLICY "Enable insert for authenticated users" ON servidores FOR INSERT WITH CHECK (true);
CREATE POLICY "Enable insert for authenticated users" ON aplicaciones FOR INSERT WITH CHECK (true);
CREATE POLICY "Enable insert for authenticated users" ON ficheros FOR INSERT WITH CHECK (true);