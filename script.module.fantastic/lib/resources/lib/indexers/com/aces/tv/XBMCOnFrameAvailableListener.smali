.class public Lcom/aces/tv/XBMCOnFrameAvailableListener;
.super Ljava/lang/Object;
.source "XBMCOnFrameAvailableListener.java"

# interfaces
.implements Landroid/graphics/SurfaceTexture$OnFrameAvailableListener;


# direct methods
.method public constructor <init>()V
    .locals 0

    .prologue
    .line 6
    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method

.method private declared-synchronized signalNewFrame(Landroid/graphics/SurfaceTexture;)V
    .locals 1

    .prologue
    .line 12
    monitor-enter p0

    :try_start_0
    invoke-virtual {p0, p1}, Lcom/aces/tv/XBMCOnFrameAvailableListener;->_onFrameAvailable(Landroid/graphics/SurfaceTexture;)V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    .line 13
    monitor-exit p0

    return-void

    .line 12
    :catchall_0
    move-exception v0

    monitor-exit p0

    throw v0
.end method


# virtual methods
.method native _onFrameAvailable(Landroid/graphics/SurfaceTexture;)V
.end method

.method public onFrameAvailable(Landroid/graphics/SurfaceTexture;)V
    .locals 0

    .prologue
    .line 18
    invoke-direct {p0, p1}, Lcom/aces/tv/XBMCOnFrameAvailableListener;->signalNewFrame(Landroid/graphics/SurfaceTexture;)V

    .line 19
    return-void
.end method
