import { ConnectorEntity } from '../entities/connector.entity.js';

export interface IConnectorStateRepository {
  save(connector: ConnectorEntity): Promise<void>;
  findById(id: string): Promise<ConnectorEntity | null>;
  findAll(): Promise<ConnectorEntity[]>;
  findByShapeId(shapeId: string): Promise<ConnectorEntity[]>;
  delete(id: string): Promise<boolean>;
  deleteByShapeId(shapeId: string): Promise<number>;
  clear(): Promise<void>;
}
