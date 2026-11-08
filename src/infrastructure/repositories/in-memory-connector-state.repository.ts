import { IConnectorStateRepository } from '../../domain/repositories/connector-state.repository.js';
import { ConnectorEntity } from '../../domain/entities/connector.entity.js';

export class InMemoryConnectorStateRepository implements IConnectorStateRepository {
  private connectors: Map<string, ConnectorEntity> = new Map();

  async save(connector: ConnectorEntity): Promise<void> {
    this.connectors.set(connector.id, connector);
  }

  async findById(id: string): Promise<ConnectorEntity | null> {
    return this.connectors.get(id) ?? null;
  }

  async findAll(): Promise<ConnectorEntity[]> {
    return Array.from(this.connectors.values());
  }

  async findByShapeId(shapeId: string): Promise<ConnectorEntity[]> {
    return Array.from(this.connectors.values()).filter(c => c.involvesShape(shapeId));
  }

  async delete(id: string): Promise<boolean> {
    return this.connectors.delete(id);
  }

  async deleteByShapeId(shapeId: string): Promise<number> {
    let deleted = 0;
    for (const [id, c] of Array.from(this.connectors.entries())) {
      if (c.involvesShape(shapeId)) {
        this.connectors.delete(id);
        deleted++;
      }
    }
    return deleted;
  }

  async clear(): Promise<void> {
    this.connectors.clear();
  }
}
