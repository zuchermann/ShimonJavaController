package innards;


/**
 * This interface defines a few important interfaces that are used throughout
 * the system for defining Keys, which are used for interacting with objects
 * such as DataRecords and the ContextTree.
 * <p>
 * Interfaces which extend from these interfaces typically define a
 * number of <code>public static final Key</code> objects for accessing contexts
 * or fields in objects such as the ContextTree that are associated with the
 * functioning of a particular system or group of systems.
 * <p>
 * Systems or objects that want access to these contexts should implement the
 * interfaces which define the desired Keys.  If you find yourself explicitly
 * qualifying a Key name, stop!  Implement the Key's interface, and access the
 * Key through the local scope.
 * <p>
 * Why do things this way?  For one, it makes the relationships between systems
 * much more explicit. Systems that share data will want access to shared Keys
 * and will thus implement interfaces that refer to each other's Keys. Thus this
 * approach makes the relationships between different systems more explicit
 * while maintaining flexibility, by providing semantic labels for functional
 * groups. Also, since we can determine which interfaces a class implements
 * automatically, we can procedurally generate documentation for important
 * fields and contexts.
 * <p>
 * @see Key
 * @see innards.namespace.context.ContextTree
 * @see innards.data.iDataRecord
 * 
 * @author synchar
 */
public interface iKeyInterfaces
{

	/** For convenience when importing **/
	public interface All extends LocalFields, DataFields, DataNames, DataValues, Context {}
	
	/**
	 * provides access to the <code>Key</code> which defines the
	 * <code>ContextTree</code> context for a particular system.
	 * <p>
	 * the system will be assumed to be in this context for the duration of its
	 * processing.  a common example are <code>Updateable</code> systems, which
	 * will typically enter the context on the first line of their update()
	 * methods, and exit the context on the last line of their update() methods.
	 * <p>
	 * @see iUpdateable
	 */
	public interface Context
	{
	}

	/**
	 * provides access to the <code>Key</code> objects which define the fields
	 * in the local context from which the input data for the system is read.
	 */	
	public interface Read
	{
	}
	
	/**
	 * provides access to the <code>Key</code> objects which define the
	 * <code>ContextTree</code> fields into which the output data for the system
	 * is written.  this data will typically be written into the context
	 * enclosing the local context for the system, so that it can be accessed by
	 * sibling systems.
	 */
	public interface Write
	{
	}
	
	/**
	 * provides access to the Keys which define the fields in the local context
	 * which contain data used by the system and its subsystems
	 */
	public interface LocalFields
	{
	}
	
	/**
	 * provides access to the Keys which define the names of many DataRecords
	 * (generally those that were generated by input devices)
	 * @see innards.data.iDataRecord
	 * @see DataFields
	 */
	public interface DataNames
	{
	}

	/**
	 * provides access to the Keys which define the fields of DataRecords
	 * produced or used by the system or device.
	 * @see innards.data.iDataRecord
	 */
	public interface DataFields
	{
	}
	
	/**
	 * provides access to the Keys which define the data values of DataRecords
	 * produced or used by the system or device.  for when you're using Keys
	 * as enumerated types.
	 * @see innards.data.iDataRecord
	 */
	public interface DataValues
	{
	}	
}